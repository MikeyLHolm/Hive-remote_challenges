/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mlindhol <mlindhol@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:36:01 by mlindhol          #+#    #+#             */
/*   Updated: 2020/03/23 14:36:01 by mlindhol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int     hv_necklace(char *s1, char *s2);

int     main(void)
{
    printf("%d\n", hv_necklace("nicole", "icolen"));
    printf("%d\n", hv_necklace("nicole", "lenico"));
    printf("%d\n", hv_necklace("nicole", "coneli"));
    printf("%d\n", hv_necklace("aabaaaaabaab", "aabaabaabaaa"));
    printf("%d\n", hv_necklace("abc", "cba"));
    printf("%d\n", hv_necklace("xxyyy", "xxxyy"));
    printf("%d\n", hv_necklace("xyxxz", "xxyxz"));
    printf("%d\n", hv_necklace("x", "x"));
    printf("%d\n", hv_necklace("x", "xx"));
    printf("%d\n", hv_necklace("x", ""));
    printf("%d\n", hv_necklace("", "")); 
    return (0);
}